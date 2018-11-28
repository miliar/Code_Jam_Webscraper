#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ULLI;
typedef long long int LLI;

int main(int argc, char** argv)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    ULLI n;
	cin >> n;
	for(ULLI i=0; i<n; i++)
	{
		string num;
		cin >> num;
		for(ULLI j = num.length()-1; j>0; j--)
		{
			if(num[j] < num[j-1])
			{
				for(ULLI k=j; k<num.length(); k++)
				{
					num[k] = '9';
				}
				num[j-1] -= 1;
			}
		}
		cout << "Case #" << i+1 << ": " << stoul(num) << endl;
	}
    return 0;
}
