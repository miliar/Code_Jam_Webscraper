#include <iostream>
#include <fstream>
using namespace std;
bool isnum(long long int a)
{
    long long int d=a;
    int len=0;
    while(d>0)
    {
       d=d/10;
        len++;
            }
    long long int b=a;
    int *arr=new int[len];
    for(int i=0;i<len;i++)
    {
        arr[i]=b%10;
        b=b/10;
    }
    int flag=0;
    for(int j=0;j<len-1;j++)
    {
        if(arr[j]<arr[j+1])
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
    {
        return false;
    }
    else
    {
        return true;
    }

}
int main()
{

//   long long int a=111111111111111110;
/*ifstream ifi;
ifi.open("a.txt");
ofstream out;
out.open("ans.txt");*/
int t;
cin>>t;
//ifi>>t;
for(int h=1;h<=t;h++)
{
    long long int a;
    cin>>a;
  // ifi>>a;
   long long int b=a;
   while(b>0)
   {
        int s=isnum(b);
        if(s==0)
        {
            b--;
        }
        else{
            cout<<"Case #"<<h<<": "<<b;
           // out<<"Case #"<<h<<": "<<b<<endl;

            break;
        }

   }
    cout<<endl;
}


 //   cout << "Hello world!" << endl;
    return 0;
}
