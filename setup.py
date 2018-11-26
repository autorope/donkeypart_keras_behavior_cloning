from setuptools import setup, find_packages

setup(name='donkeypart_keras_behavior_cloning',
      version='0.1.3',
      description='Library to control steering and throttle actuators.',
      long_description="no long description given",
      long_description_content_type="text/markdown",
      url='https://github.com/autorope/donkeypart_PCA9685_actuators',
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',
      entry_points={
          'console_scripts': [
              'donkey=donkeycar.management.base:execute_from_command_line',
          ],
      },
      install_requires=['numpy',
                        'tensorflow==1.11',
                        ],

      extras_require={'dev': ['pytest-cov']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars datastore',
      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
