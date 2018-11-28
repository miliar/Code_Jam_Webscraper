#include <bits/stdc++.h>
#define llg long long int
using namespace std;

string s;

vector<llg> v;

llg T;

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	cin>>T;

	for(llg t = 1; t <= T; t ++) {

	v.clear();

	cin>>s;

	for(llg i = 0; i < s.size(); i++) v.push_back(s[i] - '0');

	for(llg i = v.size() - 1; i >= 0; i--)
	{
		llg maior = v[i];

		for(llg j = i - 1; j >= 0; j--)
		{
			//cout<<j<<"\n";
			if(v[j] > maior)
			{
				v[j] --;

				for(llg k = j + 1; k < v.size(); k++)
				{
					v[k] = 9;
				}

				break;
			}
		}
	}

	llg first = 0;

	cout<<"Case #"<<t<<": ";

	for(llg i = 0; i < v.size(); i++)
	{
		if(first == 0 && v[i] == 0) continue;

		cout<<v[i];

		first = 1;
	}

	cout<<"\n";

	}
}