#include<iostream>
#include<vector>
using namespace std;

int main()
{
  int n;
  cin>>n;
  for(int k=0;k<n;k++)
  {
    string input;
    cin>>input;
    for(int i=0;i<input.length()-1;i++)
    {
      if(input[i]>input[i+1])
      {
        int z = i;
        while(z>0 && input[z]==input[z-1])
          z--;
        i=z;
        input[i] --;
        for(int j=i+1;j<input.length();j++)
        {
          input[j] = '9';
        }
        break;
      }
    }
    if(input[0] == '0')
      input.erase(0,1);
    cout<<"case "<<"#"<<k+1<<": "<<input<<endl;
  }
  return 0;
}
