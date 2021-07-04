from setuptools import setup, find_packages


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


if __name__ == '__main__':
    setup(name='BboxToolkit',
          version='2.0',
          description='a tiny toolkit for spcial bounding boxes',
          long_description=readme(),
          long_description_content_type='text/markdown',
          author='jbwang1997',
          author_email='jbwang1997@gmail.com',
          keywords='computer vision, object deteciton',
          url=' https://github.com/jbwang1997/BboxToolkit',
          packages=find_packages(),
          license='Apache License 2.0',
          python_requires='>=3.5',
          install_requires=[
              'pathos',
              'opencv-python',
              'terminaltables',
              'shapely',
              'numpy'])
