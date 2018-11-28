#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define OO 2000;
#define md 1000000007

bool isAllq(string str)
{
	for(int i=0; i<str.size(); i++)
		if(str[i] != '?')
			return false;
	return true;
}

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t,row,col;
  char h;
  string str;
  vector<string> vec;

  cin>>t;
  for(int tt=0; tt<t; tt++)
  {
	  vec.clear();
	  cin>>row>>col;
	  for(int j=0 ;j<row; j++)
	  {
		  cin>>str;
		  vec.push_back(str);
	  }

	  for(int r=0; r<row; r++)
	  {
		  if(!isAllq(vec[r]) && vec[r].find_first_of("?")!=std::string::npos)
		  {
			  for(int c=0; c<col; c++)
			  {
				  //convert all after h
				  if(vec[r][c] != '?')//get 1st char
				  {
					  while(c<col && vec[r][c] != '?')//move till we get to '?'
						  c++;

					  h=vec[r][c-1];
					  int sz=0,st=c;
					  string rep="";
					  while(c<col && vec[r][c]=='?')
					  {
						  c++;
						  rep+=h;
						  sz++;
					  }
					  c--;
					  vec[r].replace(st,sz,rep);
				  }
			  }
			  if(vec[r][0]=='?')//sala7 eli  fel awel
			  {
				  int tmpIndx=0;
				  while(vec[r][tmpIndx]=='?')
					  tmpIndx++;
				  h=vec[r][tmpIndx];
				  for(int tmp=0; tmp<tmpIndx; tmp++)
					  vec[r][tmp]=h;
			  }

		  }
	  }
	  //taslee7 el rwos el fadya
	  for(int i=0; i<row; i++)
	  {
		if(isAllq(vec[i]))
		{
			int st=i;
			while(i<row && isAllq(vec[i]))
			{
				i++;
			}
			string rep = (i==row)? vec[st-1] : vec[i];
			for(int ii=st; ii<i; ii++)
				vec[ii]=rep;
		}
	  }
	  cout<<"Case #"<<tt+1<<":"<<endl;
	  for(int p=0; p<row; p++)
		  cout<<vec[p]<<endl;

  }
  return 0;
}
