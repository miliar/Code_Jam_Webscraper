#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <list>
#include <fstream>
#include <map>
#include <queue>
#include <iomanip>
#include <algorithm>
#include <cmath>
using namespace std;

#define ll long long
#define mod 1000000007
#define infinity (ll)1e9+1
#define pdd pair<double,double>
#define pll pair<ll, ll>
#define pii pair<int,int>
#define MP make_pair
#define vi vector<ll>

#define FOR(i,a,b) for(ll i = (a); i < (b); ++i)
#define RFOR(i,b,a) for(ll i = (b) - 1; i >= (a); --i)
#define REPEAT(i) FOR(counter1234,0,i)
#define ALL(a) a.begin(), a.end()


int main()
{
	//ofstream out("Out.txt");
	//ifstream in("In.txt");
	int t; cin >> t;
	vector<string> ans;

	FOR(counter, 0, t)
	{
		string n;
		cin >> n;
		
		if (n.length() == 19)
			ans.push_back("999999999999999999");
		else
		{
			int index = -1;
			FOR(i,0,n.length() - 1)
				if (n[i] > n[i + 1])
				{
					index = i;
					break;
				}

			if (index == -1)
				ans.push_back(n);
			else
			{
				if (index == 0)
				{
					if (n[0] != '1')
					{
						string toPush = "";
						toPush += (n[0] - 1);
						FOR(i, 1, n.length())
							toPush += "9";

						ans.push_back(toPush);
					}
					else
					{
						string toPush = "";
						FOR(i, 1, n.length())
							toPush += "9";

						ans.push_back(toPush);
					}
				}
				else
				{
					if (n[index] != n[index-1])
					{
						string toPush = "";
						FOR(i, 0, index)
							toPush += n[i];

						toPush += (n[index] - 1);
						FOR(i, index + 1, n.length())
							toPush += '9';

						ans.push_back(toPush);
					}
					else
					{
						if (n[0] == n[index])
						{
							if (n[0] != '1')
							{
								string toPush = "";
								toPush += (n[0] - 1);
								FOR(i, 1, n.length())
									toPush += "9";

								ans.push_back(toPush);
							}
							else
							{
								string toPush = "";
								//toPush += (n[0] - 1);
								FOR(i, 1, n.length())
									toPush += "9";

								ans.push_back(toPush);
							}
						}
						else
						{
							string toPush = "";

							int last = -1;
							RFOR(i, index, 0)
								if (n[i] != n[index])
								{
									last = i + 1;
									break;
								}

							FOR(i, 0, last)
								toPush += n[i];

							toPush += (n[index] - 1);
							FOR(i, index + 1, n.length())
								toPush += '9';

							ans.push_back(toPush);
						}


					}
				}
			}
		}	
	}

	FOR(i, 0, t)
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;

	return 0;
}