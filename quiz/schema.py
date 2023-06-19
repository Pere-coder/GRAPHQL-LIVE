import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer



class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")
    
    
    
    
class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")
    
    

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")
    
    
    
class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fileds = ("question", "answer_text")
        
        
  
    
class Query(graphene.ObjectType):
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())
    all_quizzes = graphene.List(QuizzesType)
  
    
    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)
    
    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()
    

# class CategoryMutation(graphene.Mutation):
    
#     class Arguments:
#         name = graphene.String(required=True)
#     category = graphene.Field(CategoryType)
        
#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)
        
   
# class QuizzesMutation(graphene.Mutation):
    
#     class Arguments:
#         title = graphene.String(required=True)
#         category_id = graphene.ID(required=True)
#     quizzes= graphene.Field(QuizzesType)
    
#     @classmethod
#     def mutate(cls, root, info, title, category_id):
#         category = Category.objects.get(id=category_id)
#         quizzes = Quizzes(title=title, category=category)
#         quizzes.save()
#         return QuizzesMutation(quizzes=quizzes)
        
   
# class QuestionMutation(graphene.Mutation):
    
#     class Arguments:
#          title = graphene.String(required=True)
#          quiz_id = graphene.ID(required=True)
#     questions = graphene.Field(QuestionType)
    
#     @classmethod
#     def mutate(cls, root, info, title, quiz_id):
#         quiz = Quizzes.objects.get(id=quiz_id)
        
#         questions = Question(title=title, quiz=quiz)
#         questions.save()
#         return QuestionMutation(questions=questions)
    
    

class CategoryMutation(graphene.Mutation):
    
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)
        
    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)
        
              
class Mutation(graphene.ObjectType):
    
    update_category = CategoryMutation.Field()
    # update_quiz = QuizzesMutation.Field()
    # update_question = QuestionMutation.Field()
    
   


    
    
schema = graphene.Schema(query=Query, mutation=Mutation)
