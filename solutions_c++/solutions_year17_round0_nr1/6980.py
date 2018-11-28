#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    string s,s1,s2;
    int k;
    int siz,counter;
    long long int result1,result2;
    bool condition1,condition2;

    //ofstream inputF("input.txt");


    for(int l=0;l<t;l++)
    {


        cin>>s;
        scanf("%d", &k);

        siz = s.size();
        s1 = s;
        s2 = s;

        result1 = 0;
        result2 = 0;

        //left to right
        for(int i=0;i<siz;i++)
        {
            if(i+k-1>=siz)
            {
                break;
            }

            if(s1[i]=='-')
            {
                s1[i] = '+';
                counter = 0;
                for(int j=i+1;counter<k-1;j++)
                {
                    if(s1[j]=='+')
                    {
                        s1[j] = '-';
                    }
                    else
                    {
                        s1[j] = '+';
                    }
                    counter++;
                }
                result1++;
            }
            //each iteration

            //cout<<"after each iteration:\n";
            //cout<<s1<<endl;

        }
        condition1 = true;
        for(int i=0;i<siz;i++)
        {
            if(s1[i]=='-')
            {
                condition1 = false;
                break;
            }
        }
        //right to left
        for(int i=siz-1;i>=0;i--)
        {
            if(i-k+1<0)
            {
                break;
            }

            if(s2[i]=='-')
            {
                s2[i] = '+';
                counter = 0;
                for(int j=i-1;counter<k-1;j--)
                {
                    if(s2[j]=='+')
                    {
                        s2[j] = '-';
                    }
                    else
                    {
                        s2[j] = '+';
                    }
                    counter++;
                }
                result2++;
            }
            //each iteration

            //cout<<"after each iteration 2:\n";
            //cout<<s2<<endl;

        }
        //
        condition2 = true;
        for(int i=0;i<siz;i++)
        {
            if(s2[i]=='-')
            {
                condition2 = false;
                break;
            }
        }

        if(condition1==true&&condition2==true)
        {
            if(result1<result2)
            {
                //inputF<<"Case #"<<l+1<<": "<<result1<<endl;

                cout<<"Case #"<<l+1<<": "<<result1<<endl;
            }
            else
            {
               // inputF<<"Case #"<<l+1<<": "<<result2<<endl;
                cout<<"Case #"<<l+1<<": "<<result2<<endl;
            }
        }
        else if(condition1==true)
        {
            //inputF<<"Case #"<<l+1<<": "<<result1<<endl;
            cout<<"Case #"<<l+1<<": "<<result1<<endl;
        }
        else if(condition2==true)
        {
            //inputF<<"Case #"<<l+1<<": "<<result2<<endl;
            cout<<"Case #"<<l+1<<": "<<result2<<endl;
        }
        else
        {
            //inputF<<"Case #"<<l+1<<": IMPOSSIBLE"<<endl;
            cout<<"Case #"<<l+1<<": IMPOSSIBLE"<<endl;
        }

    }
}
