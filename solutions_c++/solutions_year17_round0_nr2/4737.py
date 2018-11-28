#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	freopen("input.in", "r", stdin); 
	freopen("output.out", "w", stdout);
	int T;
	cin>>T;
	for(int k=1; k<=T; k++)
	{
	    string S;
	    cin>>S;
	    int size = S.size();
	    for(int i=size-1; i>0; i--)
	    {
	        if(S[i-1]>S[i])
	        {
	            //cout<<i<<"*";
	            for(int j=i; j<size; j++)
	            {
	                S[j]='9';
	            }
	            if(S[i-1]!='0')
	            {
	                S[i-1]=(S[i-1]-1);
	            }
	            else
	            {
	                int j=i-1;
	                while(j>=0&&S[j]=='0')
	                {
	                    S[j]='9';
	                    j--;
	                }
	                if(j>=0)
	                {
	                    S[j]=S[j]-1;
	                }
	                i=j;
	            }
	        }
	    }
	    int idx;
	    for(int i=0; i<size; i++)
	    {
	        if(S[i]!='0')
	        {
	            idx=i;
	            break;
	        }
	    }
	    cout<<"Case #"<<k<<": ";
	    for(int i=idx; i<size; i++)
	    {
	        cout<<S[i];
	    }
	    cout<<endl;
	}
    return 0;
}
