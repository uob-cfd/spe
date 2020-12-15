test = {
  'name': 'Question 06_classify_role',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to define 'classify_role'
          >>> 'classify_role' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> classify_role(titanic.iloc[0])
          '3rd'
          >>> classify_role(titanic.iloc[6])
          '2nd'
          >>> classify_role(titanic.iloc[-1])
          'catering'
          >>> classify_role(titanic.iloc[-3])
          'engineering'
          >>> classify_role(titanic.iloc[-4])
          'catering'
          >>> classify_role(titanic.iloc[-5])
          'deck'
          >>> is_brailey = titanic['name'].str.startswith('Brailey')
          >>> classify_role(titanic[is_brailey].iloc[0])
          'musician'
          >>> is_andrews = titanic['name'] == 'Andrews, Mr. Thomas'
          >>> classify_role(titanic[is_andrews].iloc[0])
          'guarantee'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # More checks
          >>> labels = titanic.apply(classify_role, axis='columns')
          >>> counts = labels.value_counts()
          >>> list(counts.index) == ['3rd', 'catering', 'engineering', '1st',
          ...                        '2nd', 'deck', 'guarantee', 'musician']
          True
          >>> np.all(counts == [709, 500, 324, 321, 270, 66, 9, 8])
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
