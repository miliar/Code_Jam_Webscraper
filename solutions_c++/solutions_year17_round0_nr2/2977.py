#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,Case = 1;
	scanf("%d" ,&t);
	while(t--)
	{
		string st;
		cin>>st;
		int len = st.size(); 
		printf("Case #%d: ",Case);Case++;
		int position = len;
		if(len == 1)
			cout<<st<<endl;
		else{
			for(int i = 0; i < len-1; i++)
			{
				if(st[i] > st[i+1])
				{position=i+1;break;}	
			}
		
		if(position != len)
		{
			for(int i = position; i < len; i++)
				st[i] = '9';
			int newposition, samechar = 1;
			for(int i = position-1; i > 0; i--)
			{
				if(st[i] != st[i-1])
				{
					newposition = i;
					samechar = 0;
					break;
				}
			}
			if(!samechar)
			{
				for(int i = newposition+1; i<position; i++)
					st[i] = '9';
				st[newposition]--;
				cout<<st<<endl;
			}
			else
			{
				for(int i = 1; i < position; i++)
    			    st[i]='9';
    			st[0]--;
    			if(st[0]=='0')
    			{
			        for(int i = 1; i < len; i++)
			       		cout << st[i];
			       	cout<<endl;
			    }
			    else
			    	cout<< st << endl;
			}
		}
		else
		{
		    cout << st << endl;
		}
		}
	}
	return 0;
}