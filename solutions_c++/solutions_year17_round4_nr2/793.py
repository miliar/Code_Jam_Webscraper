#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <utility>

using namespace std;

pair<int,int> getAnswer();

int main()
{
  int num_tests;
  cin >> num_tests;
  for (int test = 1; test <= num_tests; test++) {
    pair<int,int> answer = getAnswer();
    cout << "Case #" << test << ": " << answer.first << ' ' << answer.second << "\n";
  }
  return 0;
}

pair<int,int> getAnswer()
{
  int num_seats, num_people, num_tickets;
  cin >> num_seats >> num_people >> num_tickets;
  assert(num_people == 2);
  vector<vector<int> > ticks(num_people);
  for (int i = 0; i < num_tickets; i++) {
    int pos, person;
    cin >> pos >> person;
    person--;
    ticks[person].push_back(pos);
  }
  if (ticks[0].size() > ticks[1].size())
    swap(ticks[0], ticks[1]);
  for (int i = 0; i < ticks.size(); i++)
    sort(ticks[i].begin(), ticks[i].end());
  reverse(ticks[1].begin(), ticks[1].end());
  
  int answer = ticks[1].size(), num_promos;

  int start = -1, end = 0;
  for (int i = 0; i < ticks[0].size(); i++) {
    if (ticks[0][i] == ticks[1][i]) {
      end =  i;
      if (start < 0)
	start = i;
    }
  }
  if (start < 0)
    return make_pair(answer, 0);

  int num_fix = 0;
  for (int i = 0; i < ticks[0].size(); i++)
    if (ticks[0][i] != ticks[0][start] && ticks[1][i] != ticks[0][start])
      num_fix++;
  for (int i = ticks[0].size(); i < ticks[1].size(); i++)
    if (ticks[1][i] != ticks[0][start])
      num_fix++;

  int num_need = end + 1 - start;
  if (num_fix >= num_need)
    return make_pair(answer, 0);
  else if (ticks[0][start] > 1)
    return make_pair(answer, num_need - num_fix);
  else
    return make_pair(answer + num_need - num_fix, 0);
}

