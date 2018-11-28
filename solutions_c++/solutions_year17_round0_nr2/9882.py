#include <iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{ifstream fin("B-small-attempt1.in.txt");
ofstream fout("B-small-attempt1.out.txt");
    int t;
    fin>>t;
  //  cin>>t;
  int n_int;
    for(int i=0;i<t;i++)

    {fout << "Case #" << i+1 << ": ";
        fin>>n_int;
       //  cin>>n_int;
        while(n_int>=1)
        {
int n=n_int;
        int na[5];
        int j=0;
         int flag=0;
        if(n/10==0)
        {

            fout<<n<<endl;
            flag=1;
        }
        while(n>0&&flag==0)
        {
            na[j++]=n%10;
          //  cout<<na[j-1]<<"  " ;
            n=n/10;
        }
       // cout<<endl;

        for(int k=0;k<j-1;k++)
        {
          if(na[k]>=na[k+1])
          {
              if(k==j-2)
              {
                 // cout<<n_int<<endl;
                  fout<<n_int<<endl;
                  flag=1;
                  break;
              }

          }
                        else{
                break;
              }

        }
        if(flag==0)
        {
        n_int--;
        }
        if(flag==1)
        {
            break;
        }
        }

    }
return 0;
}
