//#include<fstream>
#include <iostream>
#define lol long long
#define uol unsigned long long
#define lod long double
using namespace std;

bool cal(int G)
{
  do
  {
    int r=G%10;
    G/=10;
    int j=G%10;
    if(r<j)
        return false;
  }while(G!=0);
  return true;
}

int main()
{
//    ifstream cin("B-small-attempt0.in");
//    ofstream cout("out.txt");
    bool cal(int);
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
       // cout<<"Test case: "<<i;
        int K,j;
        cin>>K;
        for(j=K;j>0;j--)
        {
            if(cal(j))
            {
                cout<<"Case #"<<i<<": "<<j<<endl;
                break;
            }
            j=(j/10)*10;
        }
    }
	return 0;
}
