#include<iostream>
using namespace std;

int pancake(string S , int K)
{
	int n=S.length();
	int count=0;
	int i=0 ,j;
    while(i <= n-K)
    {
    
        if(S[i]=='-')
        {
        	
            for(j=i ; j < K+i ; ++j)
            {

                if(S[j]=='-')
                    S[j]='+';
                    
                

                else
                {
                    S[j]='-';
				}
					

            }
        
            
            count++;
         	
        }
        
        i+=1;
           
    }
    

    for(int j=i ; j < n ; ++j)   
    {
        if(S[j]=='-')
            return -1;
    }

    return count;
}

int main()
{
	int T,K;
	string S;
	cin>>T;

	for(int i=1;i<=T;i++)
    {
        cin>>S;
        cin>>K;
        int result = pancake(S,K);
        cout<<"Case #"<<i<<": ";
        if (result == -1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<result<<endl;
    }

    return 0;
}

