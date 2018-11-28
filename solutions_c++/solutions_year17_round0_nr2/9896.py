#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("salida.txt");
    unsigned long long t,j,n,k,dies,a,b,d,c;

    in>>t;
    for(j=1;j<=t;j++)
    {
        dies=10;
        in>>n;

        b=n%10;
        while(n/dies>=1)
        {
            a=(n%(dies*10));
            a/=dies;
            b=(n%dies);
            b/=(dies/10);
            if(!(a<=b) )
            {
                a--;
                d=n%dies;
                n/=(dies*10);
                n*=(dies*10);

                n+=a*dies;
                n+=d;
                c=dies/10;
                while(c>=1)
                {

                n/=(c*10);
                n*=(c*10);
                n+=9*c;

                c/=10;
                }

            }



           dies*=10;


        }
        out<<"Case #"<<j<<": "<<n<<endl;
    }
in.close();
out.close();

     return 0;
}
