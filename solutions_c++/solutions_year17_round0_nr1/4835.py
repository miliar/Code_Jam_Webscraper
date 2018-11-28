#include <iostream>
#include <string>


using namespace std;


int main()
{
	string S;

	int T,p,K,count=0, flag = 0,si;


	cin >> T;

	for(int i=0; i<T; i++)
	{

		cin>>S;
		cin>>K;
		si = S.size();
	
	//	cout<< S[2];
		
		
        cout<< "Case #"<<i+1<<": ";

	    for(int j=0; j< si; j++)
	    {
	    	if(S[j]=='-')
	    	{

	    		
	    		
	    		if(si - j  < K )
	    			{
	    				cout<<"Impossible"<<endl;
	    				flag=1;
	    				break;
	    			}


	    	   count ++;



	    		for(int k=j; k<j+K; k++)
	    		{


	    			if(S[k]=='-')
	    			{
	    				S[k] = '+';
	    			}

	    			else
	    			{
	    				S[k]='-';
	    			}

	    		}


	    	}




	    }


	    if(flag==0)
	    	cout<< count<< endl;


	    count=0;
	    flag=0;

	}
}