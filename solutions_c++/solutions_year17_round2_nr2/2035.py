#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("inputB.txt", "r", stdin);
    freopen("outputB.txt", "w", stdout);

	int test;

	cin>>test;

	for(int cas = 1; cas<=test; cas++)
	{
		int n, r, o, y, g, b, v;

		cin>>n>>r>>o>>y>>g>>b>>v;

		int mx = max(r, max(y, b)), temp = n/2;
		int mn = min(r, min(y, b));

		string ans = "";

		if(mx > temp)
		{
			ans = "IMPOSSIBLE";
		}

		else
		{
			int maxi, midi, mini;

			char maxc, midc, minc;

			pair<int, char> P[3];

			P[0] = {r, 'R'};
			P[1] = {y, 'Y'};
			P[2]   = {b, 'B'};

			sort(P, P+3);

			mini = P[0].first, midi = P[1].first, maxi = P[2].first;
			minc = P[0].second, midc = P[1].second, maxc = P[2].second;


			while(maxi && midi && mini)
			{
				ans += maxc;
				ans += midc;
				ans += minc;

				maxi--, midi--; mini--;
			}

			while(maxi && midi)
			{
				{
					ans += maxc;
					ans += midc;
				}

				midi --, maxi--;
			}



			while(maxi)
            {

                for(int i = 1; i<ans.size()-1; i++)
                {
                    if(ans[i] != maxc && ans[i+1] != maxc )
                    {
                        string s = "";

                        s+=maxc;

                        ans.insert(i+1, s);
                        break;
                    }
                }

                maxi--;
            }


		}

		printf("Case #%d: ", cas);
		cout<<ans<<endl;


	}
}
