#include<iostream>
#include<fstream>

using namespace std;
int isAsc(int n)
{
    int i=0,rem, dig[1000], flag=0, flag2=0;

    while(n!=0)
    {
        rem=n%10;
        n=n/10;
        dig[i]=rem;
        i++;
    }
    for(int j=0; j<(i-1); j++)
    {
        if(dig[j]>=dig[j+1])
        {
            flag++;
        }else
        if(dig[j]==dig[j+1])
            flag2++;

    }
    if(flag==i-1)
        return 1;
    else if(flag2==i-1)
        return 1;
    else if(i==1)
        return 1;
    else
        return 0;


}
int main()
{
    ifstream file;
    ofstream fileO;
    fileO.open("output3.txt");
    file.open("B-small-attempt2.in");
    int n, tidy=0, tT;

    do
    {
        file>>tT;
    }while(tT>100 && tT<1);

    for(int i=1; i<=tT; i++)
    {

        file>>n;

        for(int i=1; i<=n; i++)
        {
            if(isAsc(i)==1)
                tidy=i;
        }
        fileO<<"case #"<<i<<": "<<tidy<<std::endl;
    }

    file.close();
    fileO.close();
    return 0;
}
