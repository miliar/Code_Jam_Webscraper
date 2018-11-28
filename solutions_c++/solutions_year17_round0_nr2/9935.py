#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

#define pb push_back
//queries
#define in(a,v) ((v).find((a)) != (v).end())

vi digits;

void fix_from(int idx){
		digits[idx-1] -= 1;
		for (int i = idx; i < digits.size(); ++i)
		{
			digits[i] = 9;
		}
		for (int i = 0; i < digits.size(); ++i)
    	{
    		if(digits[i]<digits[i-1]) fix_from(i);
    	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
    //freopen("input","r",stdin);
    //freopen("output","w",stdout);

	int t;
	string number;
    cin >> t;

    int c = 1;
    while(t--){
    	cin>> number;
    	digits.resize(number.length());
    	digits[0] = number[0]-'0';
    	for (int i = 1; i < number.length(); ++i)
    	{
    		digits[i] = number[i]-'0';
    		if(digits[i]<digits[i-1]){ 
				fix_from(i);
				break;
			}

    	}



    	cout<<"Case #"<<c<<": ";
    	int idx = 0;
    	while(digits[idx] == 0) idx++;
    	for (int i = idx; i < digits.size(); ++i)
    	{
    		cout<<digits[i];
    	}
    	cout<<"\n";

    	digits.clear();
    	c++;
    }

    return 0;
}

