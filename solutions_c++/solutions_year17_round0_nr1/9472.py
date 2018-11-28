#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
  string inp;
  int t;
  cin>>t;
  int k;
  int len;
  int cflips,tflips;
  int y=1;
  while(t--)
  { cflips = 0;
    tflips = 0;
    cin>>inp;
    cin>>k;
    int len=inp.size();
    int i;
    for(i=0;i<len-k+1;i++)
    {
      if(inp[i]=='-')
      { tflips++;
        //cout<<i<<endl;
        for(int j=i;j<i+k; j++)
        {  if(inp[j]=='-')
            inp[j] = '+';
          else
            inp[j] = '-';
          }
        //cout<<inp<<endl;
      }
      else
        continue;
    }
    int check = 1;
    for(i=0;i<len;i++)
      if(inp[i]=='-')
      {  check = 0;
        break;
      }

    if(check)
      cout<<"Case #"<<y<<": "<<tflips<<endl;
    else
      cout<<"Case #"<<y<<": IMPOSSIBLE"<<endl;
    y++;
  }
  return 0;
}
