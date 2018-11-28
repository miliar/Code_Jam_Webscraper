#include<fstream>
#include<iostream>

#include<algorithm>
#include<string>

using namespace std;
 
int main()
{
	
	int i,k,len;
    ifstream input;
    input.open("input.txt",ios::in);
    ofstream result;
    result.open("result.txt",ios::out);
    string a; 
 
    int test,iterator;
    input>>test;
    for(iterator=0;iterator<test;iterator++){
    int ward;
	int counter=0;
    
    
    int j;
    
    input>>a>>k;
    len=a.length();
   
    for(i=0;i<len;i++)
    {
        if(a[i]=='-' && (len-i)>=k)
        {
            counter++;
            for(j=i;j<k+i;j++)
            {
                if(a[j]=='-')
                    a[j]='+';
                else
                    a[j]='-';
            }
 
        }
    }
    
    ward= count(a.begin(),a.end(),'-');
   
    if(ward==0)
        {
		result<<"Case #"<<(iterator+1)<<": "<<counter<<"\n";}
    else
        {
		result<<"Case #"<<(iterator+1)<<": "<<"IMPOSSIBLE"<<"\n";}
}
input.close();
result.close();
}
