#include <bits/stdc++.h>
using namespace std;


string findNext(string s)
{
    int n = s.length();
    if(n==1)return s;
    for(int i=n-1; i>=0; i--)
    {
        if(s[i]<s[i-1])
        {
            s[i]='9';
            s[i-1]--;
            for(int j=i; j<n; j++)
                s[j]='9';
        }
    }
    if(s[0]=='0')
    {
        int i;
        for(i=0; i<n; i++)
            if(s[i]!='0')break;
        return s.substr(i, n);
    }
    return s;
}

int main() {
	long t, i;
	scanf("%ld", &t);
	for(i=1; i<=t; i++)
	{
	    string n;
	    cin>>n;
	    cout<<"Case #"<<i<<": "<<findNext(n)<<endl;
	}
	return 0;
}
