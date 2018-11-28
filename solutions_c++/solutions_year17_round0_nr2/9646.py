#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{

int num_test;
cin>>num_test;
string *nums = new string[num_test];
for(int i=0;i<num_test;i++)
{
cin>>nums[i];
}
for(int i=0;i<num_test;i++)
{

int l=nums[i].length();
for(int j=1;j>0&&j<l;)
{
if(nums[i][j]<nums[i][j-1])
{
for(int k=j;k<l;k++)
nums[i][k]='9';
nums[i][j-1]-=1;
l=j;
j=j-1;

}
else
j++;
}
if(nums[i][0]=='0')
{
for(int k=0;k<nums[i].length()-1;k++)
nums[i][k]=nums[i][k+1];
nums[i][nums[i].length()-1]='\0';
}
}
int i=0;
for(i=0;i<num_test-1;i++)
cout<<"Case #"<<(i+1)<<": "<<nums[i]<<endl;
cout<<"Case #"<<(i+1)<<": "<<nums[i];
}
