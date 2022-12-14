from setuptools import setup, find_packages


def readme():
    with open('README.md', encoding="utf-8") as f:
        return f.read()


setup(name='companieshouseapi',
      version='0.1.1',
      description='An easy, flexible wrapper around the Companies House API',
      long_description=readme(),
      url='http://github.com/lewismunday/companieshouseapi',
      author='Lewis Munday',
      author_email='lewisjohnmunday@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'requests==2.28.1',
      ],
      classifiers=[
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
      ])
