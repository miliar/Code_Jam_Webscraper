#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

bool checkMax(int r, int y, int b)
{
    if (r>y && r>b && r>(y+b))
    {
        return false;
    }
    else if (y>r && y>b && y>(r+b))
    {
        return false;
    }
    else if (b>r && b>y && b>(r+y))
    {
        return false;
    }

    return true;

}
int n,r,o,y,g,b,v;
int last,first;

void getR(fstream &outFile)
{
    --r;
    last = 1;
    outFile<<"R";
}

void getY(fstream &outFile)
{
    --y;
    last = 2;
    outFile<<"Y";
}

void getB(fstream &outFile)
{
    --b;
    last = 3;
    outFile<<"B";
}

int main(){
    fstream outFile("b.out",fstream::out);

    int tests;
    cin>>tests;

    for(int test=1;test<=tests;++test)
    {

        cin>>n>>r>>o>>y>>g>>b>>v;
        

        if (!checkMax(r,y,b))
        {
            outFile<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;   
            continue;
        }

        outFile<<"Case #"<<test<<": ";

        last = 0;
        first = 0;
        while (n>0)
        {
            --n;
            if (first == 3 && last!=3 && b>=r && b>=y)
            {
                getB(outFile);
            }

            else if (r>=y && r>=b && last!=1)
            {
                getR(outFile);
            }
            else if (y>=r && y>=b && last!=2)
            {
                getY(outFile);
            }
            else if(last !=3)
            {
                getB(outFile);
            }
            else if (last == 3)
            {
                if(r>y)
                {
                    getR(outFile);
                }
                else 
                {
                    getY(outFile);
                }
            }
            else if (last == 2)
            {
                cout<<"2"<<endl;
                if(r>b)
                {
                    getR(outFile);

                }
                else 
                {
                    getB(outFile);

                }
            }
            else 
            {
                cout<<"3"<<endl;
                if(y>b)
                {
                    getY(outFile);

                }
                else 
                {
                    getB(outFile);
                }
            }

            if (first == 0)
            {
                first = last;
            }
            if (n==0 && first == last)
            {
                cout<<"last"<<endl;
                cout<<first<<" "<<last<<endl;
            }

        }


        outFile<<endl;


    }


}