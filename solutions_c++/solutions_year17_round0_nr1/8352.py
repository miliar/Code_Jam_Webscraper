#include<cstdio>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#include<string>
#include<stack>
#include<unordered_set>

using namespace std;

int main( int argc,char **argv)
{
	int cases;
	cin >> cases;
	for(int iter = 1; iter <= cases; iter++) 
	{
		
		int k;
		string str;
		cin >> str;
		cin >> k;
		
		int ans = INT_MAX;
		int n = (int)str.length();
		string des;
		for(int i=0;i<n;i++) des.push_back('+');
	
		vector< vector<pair<int,int> > > data;
		for(int i = 0; i < n - k + 1; i++) 
		{
			vector< pair<int,int> > inp;
			for(int j = i; j < n && j+k-1 < n; j = j + k) 
			{
				inp.push_back(make_pair(j, j+k-1));
			}
			data.push_back(inp);
		}

		queue< pair<string, int> > q;
		unordered_set<string> S;
		q.push(make_pair(str,0));
		S.insert(str);

		while(!q.empty()) 
		{
				pair<string,int> P = q.front(); q.pop();

				if(P.first == des) 
				{
						ans = min(ans, P.second);
						continue;
				}

				for(int i = 0 ; i < (int)data.size(); i++) 
				{
						int n = (int)data[i].size();
						for(int j = 0; j < (1<<n);j++) 
						{
								string tstr = P.first;
								int res = 0;
								for(int p = 0; p < n;p++) 
								{
										int bs = (j & (1<<p));
										if(bs) 
										{
												bool has_neg = false;
												for(int y = data[i][p].first; y <= data[i][p].second ; y++) 
												{
														if(tstr[y] == '-') has_neg = true;
												}
												if(has_neg) 
												{
														for(int y = data[i][p].first; y <= data[i][p].second ; y++) 
														{
																if(tstr[y] == '+') tstr[y] = '-';
																else tstr[y] = '+';
														}
														res = res + 1;
												}
										}
								}
								if(S.find(tstr) == S.end()) 
								{
									S.insert(tstr);
									q.push(make_pair(tstr, res + P.second));
								}
						}
				}
		}
		if(ans == INT_MAX) 
		{
			cout << "Case #" << iter << ": IMPOSSIBLE\n";
		}
		else 
		{
			cout << "Case #" << iter << ": " << ans << endl;
		}
	}
	return 0;
}
