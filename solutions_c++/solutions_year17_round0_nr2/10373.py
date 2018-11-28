#include<iostream>
#include<cstring>
#include<cmath>
#include<fstream>

using namespace std;


int check_tidy(long long int n)
{
    int k, flag=0;
    int last= n%10;

    while(n>0)
    {
        k= n%10;
        n= n/10;

        if(k<=last)
        {
           last=k;
           continue;
        }

        else
        {
            flag=1;
            break;
        }

    }

    if(flag)
        return 0;
    else
        return 1;
}



int main()
{
    long long int n, temp;
    int T;
    int result;
    ifstream infile;
    infile.open("me1.in");

    ofstream outfile;
    outfile.open("tidy.in");
    //cin >> T;

    infile>> T;

    for(int i=0;i<T; i++)
    {
      infile >> n;

      for(long long int j=n; j>0;j--)
      {
          //cout << "j value  "<< j << endl;
          result= check_tidy(j);

          //cout<< "result came"<< " " << result << endl;
          if(result)
          {
              temp= j;
              break;
          }

      }
      //cout << temp << endl;
      outfile<<"Case #"<< (i+1)<<": "  << temp << endl;
    }

    infile.close() ;
     outfile.close();

    return 0;
}
