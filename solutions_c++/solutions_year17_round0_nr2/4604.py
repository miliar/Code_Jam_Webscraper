#include <bits/stdc++.h>
using namespace std;
long long fun(string &str)
{
    int n = str.length();
    for(int i=n-1;i>0;i--)
    {
        if(str[i] < str[i-1])
        {
            str[i-1] = str[i-1] - 1;
            for(int j=i ; j < n ; j++)
                str[j] = '9';
        }
    }
    long long ans = stoll(str);
    return ans;
}
int main() 
{
	int T,Case = 1;
	cin >> T;
	while(T--)
	{
	    long long n;
	    cin>>n;
	    string str = to_string(n);
	    long long ans = fun(str);
	    
	    cout<<"Case #"<<Case<<": "<<ans<<endl;
	    
	    Case++;
	}
	return 0;
}
