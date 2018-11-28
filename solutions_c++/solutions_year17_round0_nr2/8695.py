#include <fstream>
#include <iostream>
#include <ostream>
using namespace std;
#include <cstdlib>
#include <cstring>
int main()
{
    int nrl,i,j,k,l;
    long long int nrt;
    char cnr[20];
    char s1[]="Case #";
    char s3[]=": ";
    char s4[]="\n";
    std::ifstream fisin;
    fisin.open ("B-large.in",std::ifstream::in);
    if (!fisin.is_open())
    {std::cout << "Could not open file\n";
    return 0;}
    std::ofstream fisout;
    fisout.open ("B-large-output.txt",std::ofstream::out);
    if (!fisout.is_open())
       {std::cout <<"Nu pot deschide cout\n";
        return 0;}
    fisin.getline(cnr,5);
    nrl=atoi(cnr);
    for (i=1; i<=nrl; i++)
    {fisin.getline(cnr,20);
    k=strlen(cnr);
    if (k<=1) {j=atoi(cnr);
        fisout.write(s1,6); fisout.operator<< (i); fisout.write(s3,2); fisout.operator<< (j); fisout.write(s4,1); fisout.flush();}
    else {
        for (j=0; j<k-1; j++)
        {if (cnr[j]>cnr[j+1])
        {if (cnr[j]=='1')
        {for (l=0; l<k-1; cnr[l++]='9');
        cnr[k-1]='\0';}
        else {while (j>0 and cnr[j-1]==cnr[j]) j--;
            cnr[j]=cnr[j]-1;
        for (l=j+1; l<k; cnr[l++]='9');}
        break;}
        }
        nrt=atoll(cnr);
        fisout.write(s1,6); fisout.operator<< (i); fisout.write(s3,2); fisout.operator<< (nrt); fisout.write(s4,1);
        fisout.flush();
        }
    }
    return 0;
}

