#include <bits/stdc++.h>
using namespace std;

typedef pair<long long,long long> ii;

int arr[1000];
int arr2[1000][1000];
ii arr3[1000][1000];
int pos[1000];

bool operator<(const ii &a, const ii &b)
{
	return a.first*b.second<a.second*b.first;
}

bool operator>(const ii &a, const ii &b)
{
	return a.first*b.second>a.second*b.first;
}

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		int n,p;
		cin >> n >> p;

		for(int i=0; i<n; i++)
			cin >> arr[i];

		for(int i=0; i<n; i++)
		{
			for(int j=0; j<p; j++)
			{
				cin >> arr2[i][j];
				arr3[i][j] = ii(arr2[i][j],arr[i]);
			}
			sort(arr3[i],arr3[i]+p);
			reverse(arr3[i],arr3[i]+p);
		}

		for(int i=0; i<n; i++)
			pos[i] = 0;

		int total = 0;
		bool valid = true;
		while(valid)
		{
			int maxpos = 0;
			int minpos = 0;
			for(int i=1; i<n; i++)
			{
				if(arr3[i][pos[i]]>arr3[maxpos][pos[maxpos]])
					maxpos = i;
				if(arr3[i][pos[i]]<arr3[minpos][pos[minpos]])
					minpos = i;
			}

			int a = max((arr3[minpos][pos[minpos]].first*10 + arr3[minpos][pos[minpos]].second*11 - 1)/arr3[minpos][pos[minpos]].second/11,
			 (arr3[maxpos][pos[maxpos]].first*10 + arr3[maxpos][pos[maxpos]].second*11 - 1)/arr3[maxpos][pos[maxpos]].second/11);
			int b = min(arr3[minpos][pos[minpos]].first*10/arr3[minpos][pos[minpos]].second/9, arr3[maxpos][pos[maxpos]].first*10/arr3[maxpos][pos[maxpos]].second/9);

			if(a==0)
				a++;
			if(a>b)
			{
				pos[maxpos]++;
				if(pos[maxpos]==p)
					valid = false;
			}
			else
			{
				total++;
				for(int i=0; i<n; i++)
				{
					pos[i]++;
					if(pos[i]==p)
					{
						valid = false;
						break;
					}
				}
			}
		}

		cout << "Case #" << cn << ": " << total << endl;
	}
}