#include <iostream>
#include <fstream>

using namespace std;

int l[1000], t1, t2;

void lClear()
{
    for(int i=0;i<1000;i++)
    {
        l[i] = -1;
    }
}

void showL()
{
       // cout<<"showL\t";
        //for(int i=0;l[i] > -1;i++)
          //  cout<<l[i]<<" ";
        //cout<<endl;
}

void shift(int i, int j)
{
    //cout<<"s";

    for(int c= j;c>i;c--)
    {
        l[c] = l[c-1];
    }

}

int maxIndex(int j)
{
    int max =0, index = 0;

    for(int i=0;i<j;i++)
    {
        if(l[i]>=max)
        {
            index = i;
            max = l[i];
        }
    }
    return index;
}

void beshkoon(int i, int j)
{
  //  cout<<"b";
    if(l[i]%2 == 0)
    {
       // cout<<"z";
        shift(i,j);
        l[i+1] = ((l[i]-1)/2);
        l[i] = l[i]/2;

    }
    else
    {
     //   cout<<"f";
        shift(i,j);
        l[i] = l[i]/2;
        l[i+1] = l[i];
    }
    t1 = l[i] ;
    t2 = l[i+1];

    showL();
}

int main()
{
    ifstream in("C-small-1-attempt0.in");
    ofstream out("C-small-1-attempt0.out");


    int T;
    in>>T;

//    cout<<"t = "<<T;

    for(int i=0; i<T; i++)
    {
        lClear();
        int n,k, minV, maxV;

        in>>n;
        in>>k;

        l[0] = n;
//        cout<<"n,k"<<n<<" "<<k;
    //=============================================//

    //cout<<"next"<<endl<<endl;
        for(int j=1;j<=k;j++)
        {
            int iMax = maxIndex(j);
      //      cout<<" iMax="<<iMax<<endl;
            beshkoon(iMax,j);
        }


    maxV = t1<t2?t2:t1;
    minV = t1>t2?t2:t1;



    //==============================================//
        out<<"Case #"<<i+1<<": "<<maxV<<" "<<minV;

        if(i != T-1)
            out<<endl;
    }

    out.close();
    return 0;
}
