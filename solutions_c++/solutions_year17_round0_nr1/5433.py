#include<iostream>
#include<fstream>
using namespace std;

int main()
{

    ifstream fin;
    ofstream fout;

    fin.open("A-large.in");
    fout.open("2.txt");

    int t;
    fin >> t;

    for(int y=0;y<t;y++)
    {

        string data;
        fin>>data;
        int k, exc;
        fin>>k;

        int len = data.length();
        int f=1, cnt=0, imp;



        while(f)
        {
            for(int i=0;i<len;i++)
            {
             exc=0;
             imp=0;
            if(data[i]=='-' && i<=(len-k))
            {
                        for(int j=0;j<k;j++)
                        {
                            if(data[i+j]=='-')
                            data[i+j]='+';
                            else data[i+j]='-';
                            exc=1;

                        }
                        //cout<<"\n"<<data;
                        cnt++;
                        break;

            }
            else if(data[i]=='-' && i>(len-k))
                    {
                        exc=1;
                        imp=1;
                        f=0;
                        break;
                    }



           }
           if(exc==0)
            f=0;
        }

        if(imp)
        fout<<"Case #"<<y+1<<": IMPOSSIBLE"<<endl;

        else
            fout<<"Case #"<<y+1<<": "<<cnt<<endl;

    }


}
