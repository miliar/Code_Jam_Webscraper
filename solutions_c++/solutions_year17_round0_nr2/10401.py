#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
  freopen("B-small-attempt5.in","r",stdin);
  freopen("output_file_name.out","w",stdout);
 long long int i,j,k,lll;
 int r,ll;
 cin >>i;
 long long int l=1,s=0,count=0;
 for(int ii=0;ii<i;ii++)
 {

  cin >>j;
   lll=j;
  vector <long long int>a,b;
  while(1){
	while(j!=0)
	{


	    //if(j<9)

	    r=j%(10);
	    j=j/(10);
	    a.push_back(r);


	}
	reverse(a.begin(),a.end());
   b=a;
   sort(a.begin(),a.end());
   //cout << "sort of a"<<endl;
   /*for(int mm=0;mm<a.size();mm++)
   {

      cout <<a[mm];
   }
   cout<<endl;
    //cout<<"normal b"<<endl;
   for(int mm=0;mm<b.size();mm++)
   {

      cout<<b[mm];
   }
   cout<<endl;*/
   if(equal(a.begin(),a.end(),b.begin())){
   cout << "Case #"<<l++<<": ";
   for(int mm=0;mm<a.size();mm++)
   {

      cout << a[mm];
   }
   cout << endl;
   //cout<<"alu\n";
   break;
   }
   else{
       //cout<<"alu1\n";
       lll=lll-1;
       j=lll;
       a.clear();
       b.clear();
   }
   }
 }
}

