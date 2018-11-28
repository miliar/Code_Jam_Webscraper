#include <iostream>
#include <vector> 
#include <algorithm>

#define smaller(a, b) ((a < b) ? (a) : (b)) 
#define bigger(a, b) ((a > b) ? (a) : (b)) 

using namespace std; 

typedef vector< pair<int, int> > vp;
typedef vector< pair<pair<int, int>, int> > vpp;

void updateVpp(vp&, vpp&);

void updateVp(vector<int>&, vp&, int);

void updateVpp(vp& vec, vpp& v)
{
  int n = vec.size();
  v.clear();
  vp::iterator it = vec.begin();
  for(int i = 0; i != n; i++, it++)
  {
    int sm = smaller(it->first, it->second);
    int big = bigger(it->first, it->second);
    v.push_back(make_pair(make_pair(sm, big), n - i));
  }
}

void updateVp(vector<int>& s, vp& vec, int pos)
{
  int n = vec.size();
  s[pos] = 1;
  vec[pos] = make_pair(-1, -1);

  int left = pos - 1;
  while (left >= 0 and !s[left])
  {
    vec[left].second = pos - left - 1;
    left--;
  }
  int right = pos + 1;
  while (right < s.size() and !s[right])
  {
    vec[right].first = right - pos - 1;
    right++;
  }
}

int main() 
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t; 

	for (int x = 1; x <= t; x++)
	{
		int n, k;
		cin >> n >> k;

    vector<int> s;
    for (int i = 0; i != n; i++)
      s.push_back(0);

		vp vec;
		for (int i = 0; i != n; i++)
      vec.push_back(make_pair(i, n - i - 1));

    vpp v;
    updateVpp(vec, v);

    sort(v.begin(), v.end());

    for (int i = 0; i != k-1; i++)
    {
      int pos = n - (v.back()).second;
      updateVp(s, vec, pos);
      updateVpp(vec, v);
      sort(v.begin(), v.end());
    }
    
    pair<int, int> nums = v[n - 1].first;
    cout << "Case #" << x << ": " << nums.second << " " << nums.first << "\n";
  }

  return 0;
}


    

  		
