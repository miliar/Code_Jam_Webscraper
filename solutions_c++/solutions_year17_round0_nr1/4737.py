#include<bits/stdc++.h> //Akshita
using namespace std;
int main()
{
    int test,test1;
    scanf("%d",&test);
    test1=test;
    while(test--)
    {
        string akku;
        int found=0,gone=0,katappa,come=0,june=0;
        cin>>akku>>katappa;
        for(int io=0;io<akku.size();io++)
        {
            if(akku[io]=='-')
            {
                found=1;
                break;
            }
        }

        if(found==0)
            printf("Case #%d: 0\n",test1-test);
        else
        {
            for(int io=0;io<akku.size();io++)
            {
                if(akku[io]=='-')
                {
                    come++;
                    for(int june=io;june<=(io+katappa-1) && (io+katappa-1)<akku.size() ;june++)
                    {
                        if(akku[june]=='+')
                            akku[june]='-';
                        else
                            akku[june]='+';
                    }
                }
            }
            for(int io=0;io<akku.size();io++)
            {
                if(akku[io]=='-')
                {
                    gone=1;
                    break;
                }
            }
            if(gone!=1)
                printf("Case #%d: %d\n",test1-test,come);
            else
                printf("Case #%d: IMPOSSIBLE\n",test1-test);
        }
    }
}
