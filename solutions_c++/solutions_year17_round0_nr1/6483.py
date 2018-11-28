#include <iostream>
#include <string.h>
using namespace std;

void flip(char S[], int a, int b)
{
	for(int i=a;i<b;i++)
	{
		if(S[i]=='+')
		{
			S[i]='-';
		}

		else
		{
			S[i]='+';
		}
	}
}

int stringcheck(char S[])
{
	int count = 0;

	for(int i=0;i<strlen(S);i++)
	{
		if(S[i]=='+')
		{
			count++;
		}
	}

	return count;
}

int main()
{
    int test,itr=1;

    cin>>test;

    while(test--)
    {
        char S[10000];
        int K, add=0, sub=0, flag=0;

        cin>>S>>K;

        for(int i=0;i<strlen(S);i++)
        {
            if(S[i]=='+')
            {
                add++;
            }

            else
            {
                sub++;
            }
        }

        //cout<<add<<" "<<sub<<endl;

        cout<<"Case #"<<itr<<": ";
        itr++;

        if(add==strlen(S))
        {
            cout<<"0\n";
        }

        else if(sub==strlen(S) && sub%K==0)
        {
            cout<<sub/K<<endl;
        }

        else if(sub==strlen(S) && sub%K!=0)
        {
            cout<<"IMPOSSIBLE\n";
        }

        else
        {
        	int flipcount=0;

        	for(int j=0;j<strlen(S);j++)
        	{
        		//cout<<S<<endl;
        		if(S[j]=='-')
        		{
        			//cout<<j<<endl;

        			if(j+K<=strlen(S))
        			{
        				flip(S,j,j+K);
        				flipcount++;
        			}

        			else
        			{
        				flag = 1;
        			}

        			if(j+K==strlen(S))
        			{
        				break;
        			}
        		}
        	}

        	if(stringcheck(S)==strlen(S))
        	{
        		cout<<flipcount<<endl;
        	}

        	else
        	{
        		flag = 1;
        	}
        }

        if(flag==1)
        {
        	cout<<"IMPOSSIBLE\n";
        }
    }
}