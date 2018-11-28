#include<iostream>
#include<string.h>
using namespace std;
int count=0;

int isHappy(char str[])
{
   //cout<<"IN isHappy\n";
    int i=0;
    while(str[i]!='\0')
    {
        if(str[i++]!='+')
            return 0;
    }
    return 1;
}
void flip(char arr[],int k,int i)
{
    //cout<<"in Flip\n";
    int j;
    for(j=i;j<i+k;j++)
    {
        if(arr[j]=='+')
            arr[j]='-';
        else
            arr[j]='+';
    }
   // cout<<arr<<"\n";
}
static int  make_happy(char str[],int n,int k)
{
    //static int count=0;
   // cout<<"in MAkeHappy\n";
    int i=0;
    if(isHappy(str)==1)
    {
    //cout<<"In make_happy Count="<<count<<"\n";
    return count;
    }
    else
    {
    while(str[i]!='\0')
    {
        if(str[i]=='+')
        {
            i++;
        }
        else if((n-i)>=k)
        {
            
            flip(str,k,i);
            count++;
            make_happy(str,n,k);
        }
        else
        {
            return -1;
        }
       
    }
 }
    return count; 
}
    
        

int main()
{
    //printf("IN main\n");
  
    int i;
    int n;
    int k;
    //scanf("%d",&n);
    cin>>n;
    //printf("Helllo\n");
    for(i=1;i<=n;i++)
    {
         
        char input[1002];
        //scanf("%s",input);
        //scanf("%s",input);
        //scanf("%d",&k);
        cin>>input;
        cin>>k;
    int len=strlen(input);
    int res;
    res=make_happy(input,len,k);
        //cout<<"IN main result="<<res<<"\n";
    if(res==-1)
    {
        //printf("Case #%d: IMPOSSIBLE\n",i);
        cout<<"Case #"<<i<<": "<<"IMPOSSIBLE\n";
    }
    else
    {
        //printf("Case #%d: %d\n",i,res);
        cout<<"Case #"<<i<<": "<<res<<"\n";
    }
        count=0;
    }
    return 0;
}

