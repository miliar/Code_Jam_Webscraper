#include <iostream>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

#define debug cout

#define ll long long int

#define fori(n) for(int i = 0; i < n; i++)
#define forj(n) for(int j = 0; j < n; j++)
#define fork(n) for(int k = 0; k < n; k++)

#define forri(n) for(int i = n - 1; i >= 0; i--)
#define forrj(n) for(int j = n - 1; j >= 0; j--)
#define forrk(n) for(int k = n - 1; k >= 0; k--)
	
#define fori2(s,n) for(int i = s; i < n; i++)
#define forj2(s,n) for(int j = s; j < n; j++)
#define fork2(s,n) for(int k = s; k < n; k++)

#define forit(v) for(auto it = v.begin(); it != v.end(); it++)
#define forrit(v) for(auto it = v.rbegin(); it != v.rend(); it++)

string S;
int K;

void RunInstance()
{
	cin >> S >> K;
	
	int cpt = 0;

	fori(S.length() - K + 1) 
	{
		if(S[i] == '-') 
		{
			forj(K) {
				S[i + j] = (S[i + j] == '-') ? '+' : '-';
			}
			cpt++;
		}
	}

	fori2(S.length() - K, S.length()) 
	{
		if (S[i] == '-') {
			cout << "IMPOSSIBLE";
			return;
		}
	}

	cout << cpt;
}

// ======================================================== //

int main()
{
	int num_of_instances = 0;
	cin >> num_of_instances;

	for (int i = 1; i <= num_of_instances; ++i)
	{
		cout << "Case #" << i << ": ";
		RunInstance();
		cout << endl;
	}
}

