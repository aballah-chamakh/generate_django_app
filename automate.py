import os

# ecnter directory name
dir = input('enter the name of your django project that is located on the desktop : ')
requirements = {
'django':'django==2.0',
'DRF':'djangorestframework',
# 'jwt':'djangorestframework-jwt',
# 'cors':'django-cors-headers',
# 'channels':'channels',
}

project_path = '../{project_dir}/'.format(project_dir=dir)
if os.path.isdir(project_path) == False :
    print('this folder do not exist on the desktop directory ')
    quit()

os.chdir(project_path.format(project_dir=dir))
if os.path.isdir('venv') == False  :
    print('venv do not exist')
    os.system('virtualenv venv')

os.chdir('venv/scripts')
os.system('activate')

for k,v in requirements.items() :
    os.system('pip install {module}'.format(module=v))
os.chdir('../..')
os.system('django-admin startproject django_test')
