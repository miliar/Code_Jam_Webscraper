#include<bits/stdc++.h>
#include<string>
#define ll long long
using namespace std;
#define INF 1000000000000

int main()
{
    //ifstream cin; cin.open("file.txt"); ofstream cout; cout.open("fileout.txt"); //comment while testing.
    ll t;
    cin>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
        char str[1000];
        int k, n,count;
        cin >> str;
        cin >> k;
        n=strlen(str);
        
        count=0;
        for(int i=0; i<=n-k; i++){
        	if(str[i]=='-'){
        		for(int j=i; j<i+k; j++){
        			if((str[j]=='-'))
        				str[j] = '+';
        			else
        				str[j]='-';
        		}
        		count++;

        	}
        }
        int i;
        for( i=n-k+1; i<n; i++){
        	if(str[i]=='-')
        		break;
        }
        if(i!=n)
        	cout <<"Case #"<<testcase<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<testcase<<": "<<count<<endl; // answer
    }
    return 0;
}