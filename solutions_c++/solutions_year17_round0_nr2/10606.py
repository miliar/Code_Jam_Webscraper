#include<iostream>
#include<string.h>

using namespace std;


void stringandlength(char *s,int *l)
{


    int i;

      int j=(*l)-1;


        while(s[j]=='0')
        {

            j--;
        }
        int c;
        c=s[j];
        c--;

        s[j]=c;
        j++;

        while(j<(*l))
        {
            s[j]='9';
            j++;


        }



    if(s[0]=='0')
    {

        *l=*l-1;
    }




}
int main()
{

    int t;
    cin>>t;
   int j=1;
    while(t>0)

    {

            string n;
            cin>>n;

            int length1=n.size();
            int i_length=n.size();

            while(length1>0)
            {
                string x;
                x=n;
              int f,s;
        int flag=0,check=0;
                int length2=x.size();
              int i=length2-1;
                while(length2>0)
                {
                    if(flag==1)
                    {
                        f=s;
                        s=x[i];
                        i--;
                        length2--;

                        if(s>f)
                        {
                            check=1;
                            break;
                        }



                    }
                    if(flag==0)
                    {
                        f=x[i];
                        s=f;
                        i--;
                        length2--;
                        flag=flag+1;


                    }






                }

                if(check==0)
                {

                    break;

                }






                stringandlength(&n[0],&length1);
            }
                int i;
           cout<<"Case #"<<j<<": ";
           for(i=(i_length-length1);i<i_length;i++)
           {
               cout<<n[i];
           }
           cout<<"\n";



        t--;j++;
    }



}
