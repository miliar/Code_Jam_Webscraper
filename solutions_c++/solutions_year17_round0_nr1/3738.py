#include<iostream>

using namespace std;
void inverse( char *c)
{ 
	if (*c=='+')
		*c='-';
	else *c='+';
}


int main ()
{
	int t,k;
	int impo=0;
	string s;
	cin >> t;
	
	for (int i=0;i<t;i++)
	{
		impo=0;
		cin >> s >> k;
		int cpt=0;
		int j=0;
		while (j <= s.size()-k)
		{
			if(s[j]=='-')
			{	for (int l=0;l<k;l++)
				{inverse(&s[j+l]);}
					cpt++;
			}
			j++;
			
		}		
			 for(int l=0;l<k;l++)
				{ if(s[j+l]=='-')
					{
						impo=1;
						break;
					}
				}	
			if (impo==1)
				cout << "Case #"<< i+1 << ": " << "IMPOSSIBLE"<<endl;
			else cout << "Case #"<< i+1 << ": " << cpt<<endl;	
					
					
		
		
		
	}
	return 0;
	
	
	
	
	
	
	
	
}
