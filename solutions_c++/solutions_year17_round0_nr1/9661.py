#include <bits/stdc++.h>
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

int main(int argc, char const *argv[])
{
	freopen ("A-large.in", "r", stdin);
	freopen ("output1.out", "w", stdout);
	int t;
	cin >> t;
	int cse = 1;
	while(t--){
		string s;
		int k;
		cin >> s >> k;
		int count = 0;
		int i=0;
		for (int i = 0; i <= (s.size()-k); i++)
			{
				if (s[i]=='-')
				{
					for (int j = i; j < k+i ; j++)
					{

						if(s[j]=='+'){
							s[j]='-';
						}
						else
							s[j]='+';
					}
					count++ ;
				}
			}
		int flag=1;
		for (int i = 0; i < s.size(); i++)
			{
				if (s[i]=='-')
				{
					cout << "Case #"<<cse << ": IMPOSSIBLE"<<endl;
					flag=0;
					break;
				}
			}
		if(flag){
			cout <<"Case #" <<cse <<": " << count <<endl;
		}		
		cse++ ;			
	}
	return 0;
}
