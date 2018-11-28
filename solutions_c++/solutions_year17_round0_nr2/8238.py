#include <bits/stdc++.h>
using namespace std;
int main()
{	
	int tn,ti;
	scanf("%d",&tn);
	long long int ans=0;
	int l,i,j;
	int k;
	for(ti=1;ti<=tn;ti++)
	{
		string str;
		cin >> str;
		while(1)
		{
			//cout << str << endl;
					int outcnt=0;
		int flag = 0;

			l = str.length();
			int tobreak = 1;
			for(i=1;i<l;i++)
			{
				if(str[i]<str[i-1])
				{
					tobreak=0;
				}
			}
			if(tobreak==1)
			{
				break;
			}

			string out;
			out.push_back(str[0]);
			outcnt++;
			for(i=1;i<l;i++)
			{
				if(str[i]>=str[i-1])
				{
					out.push_back(str[i]);
					outcnt++;
				}
				else
				{
					if(str[i]=='0')
					{
						while(outcnt>0)
						{
							outcnt--;
							if(out[outcnt]>'1')
							{
								flag=1;
								break;
							}
						
						}
						string newout;
						if(flag==1)
						{
							for(k=0;k<outcnt;k++)
							{
								newout.push_back(out[k]);				
							}
							newout.push_back(out[k]-1);
							for(k = outcnt+1;k<l;k++)
							{
								newout.push_back('9');			
							}
						}
						else
						{   
							for(k=0;k<outcnt;k++)
							{
								newout.push_back(out[k]);				
							}
							for(k = outcnt;k<l-1;k++)
							{
								newout.push_back('9');			
							}	
						}
						out = newout;
						break;
					}
					else
					{
						//cout << out << endl;
						out[outcnt-1]=str[i-1]-1;			
						for(k=outcnt;k<l;k++)
						{
							out.push_back('9');			
						}	
					}
					break;
				i = l+1;
				}

			}
			str = out;
		}


		printf("Case #%d: ",ti);
		cout << str << endl;
	}
	return 0;
}