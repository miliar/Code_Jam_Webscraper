#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int maxKits(vector<int> &needed, vector<vector<int> > &packs);

int main()
{
  int num_tests;
  cin >> num_tests;
  for (int test = 1; test <= num_tests; test++) {
    int num_ings, num_packs;
    cin >> num_ings >> num_packs;
    vector<int> needed(num_ings);
    for (int i = 0; i < needed.size(); i++)
      cin >> needed[i];
    vector<vector<int> > packs(num_ings, vector<int>(num_packs));
    for (int i = 0; i < packs.size(); i++) {
      for (int j = 0; j < packs[i].size(); j++)
	cin >> packs[i][j];
      sort(packs[i].begin(), packs[i].end());
    }

    cout << "Case #" << test << ": " << maxKits(needed, packs) << '\n';

    
    // for (int i = 0; i < needed.size(); i++)
    //   cout << needed[i] << ' ';
    // cout << "\n\n";
    // for (int i = 0; i < packs.size(); i++) {
    //   for (int j = 0; j < packs[i].size(); j++)
    // 	cout << packs[i][j] << ' ';
    //   cout << '\n';
    // }
    // cout << "\n\n";
  }
      
  return 0;
}

int maxKits(vector<int> &needed, vector<vector<int> > &packs)
{
  vector<vector<pair<int,int> > > s_ranges(packs.size(), vector<pair<int,int> >(packs[0].size())); // serving ranges
  for (int i = 0; i < packs.size(); i++)
    for (int j = 0; j < packs[i].size(); j++) {
      s_ranges[i][j].first = (int)ceil(10.0 / 11.0 * (double)packs[i][j] / (double)needed[i]);
      s_ranges[i][j].second = (int)floor(10.0 / 9.0 * (double)packs[i][j] / (double)needed[i]);
    }

  // for (int i = 0; i < s_ranges.size(); i++) {
  //   for (int j = 0; j < s_ranges[i].size(); j++)
  //     cout << s_ranges[i][j].first << ' ' << s_ranges[i][j].second << "  ";
  //   cout << endl;
  // }
  
  int max_kits = 0;
  vector<int> poses(s_ranges.size(), 0);
  for (int num_servings = 1; num_servings <= 1000005; num_servings++) {
    // cout << "num servings " << num_servings << endl;
    bool works = true;
    while (works) {
      for (int i = 0; i < poses.size(); i++) {
	// cout << "hello " << i << ' ' << poses[i] << endl;
	while (poses[i] < s_ranges[i].size()) {
	  if (s_ranges[i][poses[i]].first > s_ranges[i][poses[i]].second || s_ranges[i][poses[i]].second < num_servings)
	    poses[i]++;
	  else
	    break;
	}
	// cout << "again " << num_servings << endl;
	if (poses[i] >= s_ranges[i].size()) {
	  works = false;
	  break;
	}
	else if (s_ranges[i][poses[i]].first > num_servings)
	  works = false;
      }
      if (works) {
	// cout << "got here" << endl;
	max_kits++;
	for (int i = 0; i < poses.size(); i++)
	  poses[i]++;
      }
      // cout << "here " << works << endl;
    }
  }
  return max_kits;
}

