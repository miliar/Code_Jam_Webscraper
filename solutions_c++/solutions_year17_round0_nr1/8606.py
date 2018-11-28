#include <fstream>
#include <iostream>
#include <ostream>
using namespace std;
#include <cstdlib>
#include <cstring>

int main()
{
    int nrl,i,j,k,n,ns,nrv,l;
    char cnr[1001];
    char cnk[5];
    char s1[]="Case #";
    char *p1,*p2;
    char s3[]=": ";
    char s4[]="\n";
    char s2[]="IMPOSSIBLE";
    char c2='-';
    bool bc;
    std::ifstream fisin;
    fisin.open ("A-small-attempt1.in",std::ifstream::in);
    if (!fisin.is_open())
    {std::cout << "Could not open file\n";
    return 0;}
    std::ofstream fisout;
    fisout.open ("A-small-output.txt",std::ofstream::out);
    if (!fisout.is_open())
       {std::cout <<"Nu pot deschide cout\n";
        return 0;}
    fisin.getline(cnk,4);
    nrl=atoi(cnk);
    for (i=1; i<=nrl; i++)
    {fisin.get(cnr,1001,' '); fisin.getline(cnk,5);
    k=atoi(cnk);
    p1=cnr;
    n=strlen(p1);
    ns=0;        //total number of flips for a minimal valid solution
    if (cnr[0]==c2)     //anyway the leftmost flip must be done in this case, then we start with this
    {ns=ns+1;
    for (j=0; j<k; j++)
        {if (*(p1+j)==c2) *(p1+j)='+';
    else *(p1+j)=c2;}}
    j=0; p2=p1;
    p2=strstr(p2,"+-");
    while (p2!=NULL)
    { p2+=2; j++; p2=strstr(p2,"+-");}
    p2=p1;
    p2=strstr(p2,"-+");
    while (p2!=NULL)
    { p2+=2; j++; p2=strstr(p2,"-+");}
    nrv=j;  //nrv is  (the number of groups of contiguous pancakes facing the same direction) - 1
    bc= true;
    while (bc)
    {if (nrv==0) {
        fisout.write(s1,6); fisout.operator<< (i); fisout.write(s3,2); fisout.operator<< (ns); fisout.write(s4,1); fisout.flush();
        /*cout << "Case #" << i << ": " << ns <<"\n";*/
    break;}
    p2=p1;
    p2=strstr(p2,"+-");
    if (p2!=NULL)
    {j=p2-p1;
    if (j+k>n-1)
    {fisout.write(s1,6); fisout.operator<< (i); fisout.write(s3,2); fisout.write(s2,10); fisout.write(s4,1); fisout.flush();
        /*cout << "Case #" << i << ": IMPOSSIBLE\n";*/
    break;}
    if (j+k==n-1)
    {if (nrv==1) {ns=ns+1;
        fisout.write(s1,6); fisout.operator<< (i); fisout.write(s3,2); fisout.operator<< (ns); fisout.write(s4,1); fisout.flush();
        /*cout << "Case #" << i << ": " << ns <<"\n";*/
    break;}
    else {fisout.write(s1,6); fisout.operator<< (i); fisout.write(s3,2); fisout.write(s2,10); fisout.write(s4,1); fisout.flush();
        /*cout << "Case #" << i << ": IMPOSSIBLE\n";*/
    break;}}
    else {
        if (*(p1+j+k)!=*(p1+j+k+1)) nrv=nrv-2;
        for (l=j+1; l<=j+k; l++) {
        if (*(p1+l)==c2) *(p1+l)='+';
        else *(p1+l)=c2;}
        ns=ns+1;
        }
    }
    }
}
return 0;
}

