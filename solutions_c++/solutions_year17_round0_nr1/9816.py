#include<iostream>
using namespace std;

main()
{
string s;
int k=0;

    cout<<"Enter string#"<<endl;
    cin>>s;
    cout<<"\nEnter value of k";
    cin>>k;
    int check=0, minuss=0;
    int flag=1;
    int steps=0;
int size=s.size();
        for(int i=0; i<size; i++)  //8 is size of string
        {
            for(int j=i; (j<i+k+1 &&j<size); j++)        //4 is size
            {
                if(s[j]=='+')
                {
                    check++;
                }
                if(s[j]=='-')
                {
                    minuss++;
                }
            }
            if(check==1 && check+minuss>=3)
            {
                if(s[i]=='+')
                {
                    for(int ab=i+1; ab<i+k+1; ab++)
                    {
                        s[ab]='+';
                    }
                }
                else if(s[i+k]=='+')
                {
                    for(int ab=i; ab<i+k; ab++)
                    {
                        s[ab]='+';
                    }
                }
                steps++;
            }

            if(minuss==2 && check+minuss==4)
            {
                if(s[i]=='-' && s[i+k]=='-')
                {
                    for(int t=i; t<i+k+1; t++)
                    {
                        s[t]='+';
                    }

           cout<<"hello";
               }
               steps=steps+2;
            }
cout<<s;
cout<<"\ncheck:"<<check<<"\nminus: "<<minuss;

            check=0, minuss=0;    //check is reset for second iteration
        }

cout<<"\ncheck:"<<check<<"\nminus: "<<minuss;


        for(int j=0; j<4; j++)
        {
        if(s[j]=='-')
            cout<<"Impossible";
            break;
        }
cout<<s<<"\n steps:"<<steps;

}
