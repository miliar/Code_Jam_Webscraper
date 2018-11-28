#include <iostream>
#include <string>
using namespace std;

int find(char S[])
{
	char pre = S[strlen(S)-1];
	int flag = -1;

    for(int i=strlen(S)-2;i>=0;i--)
    {
    	if(S[i]>pre)
    	{
    		flag = i;
    		break;
    	}

    	else
    	{
    		pre = S[i];
    	}
    }

    return flag;
}

int main()
{
    int test,itr=1;

    cin>>test;

    while(test--)
    {
        char S[50];
        int flag = -1;

        cin>>S;

        flag = find(S);

        while(flag!=-1)
        {
        	int update = S[flag] - '0';

	        if(S[flag+1]-'0'<update)
	        {
	        	update--;
	        }

	        S[flag] = update + '0';

	        for(int k=strlen(S)-1;k>flag;k--)
	        {
	        	S[k] = '9';
	        }

	        flag = find(S);
        }

        cout<<"Case #"<<itr<<": ";
	    itr++;

	    if(S[0]=='0' && strlen(S)!=1)
	    {
	    	for(int k=1;k<strlen(S);k++)
	    	{
	    		cout<<S[k];
	    	}

	    	cout<<endl;
	    }

	    else
	    {
	    	cout<<S<<endl;
	    }
    }
}