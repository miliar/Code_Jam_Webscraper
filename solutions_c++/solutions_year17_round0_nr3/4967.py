#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

vector<long long> indexs(long long k)
{
    vector<long long> result;

    while(k>0)
    {
        result.push_back(k);
        k>>=1;
    }
    reverse(result.begin(),result.end());
    return result;
}

void calc(fstream &outFile, int testNr, long long n,long long k)
{
    /*
    long long maxRegion = (n-k+1)/k;
    if (((n-k+1)%k) > 0)
    {
        maxRegion+=1;
    }
    maxRegion--;
*/
    long long maxRegion = n;

    int potega = -1 ;

    long long tmpK = k;
    
    while(tmpK>0)
    {
        potega++;
        tmpK>>=1;
    }
    
    //cout<<potega<<endl;

    vector<long long> index = indexs(k);
/*
    if(testNr<=4 || testNr == 97)
    {
        cout<<"N: "<<n<<" POW "<<potega<<endl;
        cout<<"index ";
        for(auto &v:index)
        {
            cout<<v<<" ";
        }
        cout<<endl;
    }
*/
    for(int i=1;i<=potega;++i)
    {
        maxRegion--;
        //if (testNr == 97)
            //cout<<maxRegion<<endl;
        if (index[i-1]*2 == index[i])
        {
            if (maxRegion%2 == 0)
                maxRegion>>=1;
            else 
            {
                maxRegion>>=1;
                maxRegion++;
            }
        }
        else 
        {
            maxRegion>>=1;
        }


    }

    maxRegion--;
    //maxRegion = (n-k+1)/(1<<(potega-1));



    cout<<testNr<<" "<<maxRegion<<" - ";

    long long podRegion = maxRegion>>1;
    
    outFile<<"Case #"<<testNr<<": ";
    if(maxRegion%2 == 0)
        outFile<<podRegion<<" ";
    else
        outFile<<(podRegion+1)<<" ";

    outFile<<(podRegion)<<endl;

}

void calc1(fstream &outFile, int testNr, long long n,long long k)
{
    vector<long long> index = indexs(k);
    long long maxRegion = n;

    int potega = index.size()-1 ;

        
    for(auto &v:index)
        cout<<v<<" ";
    cout<<endl;

    for(int i=1;i<=potega;++i)
    {
        maxRegion--;

        cout<<maxRegion<<endl;
        if (index[i-1]*2 == index[i])
        {
            if (maxRegion%2 == 0)
                maxRegion>>=1;
            else 
            {
                maxRegion>>=1;
                maxRegion++;
            }
        }
        else 
        {
            maxRegion>>=1;
        }
    }

    maxRegion--;
    cout<<testNr<<" "<<maxRegion<<" - ";

    long long podRegion = maxRegion>>1;
    
    outFile<<"Case #"<<testNr<<": ";
    if(maxRegion%2 == 0)
        outFile<<podRegion<<" ";
    else
        outFile<<(podRegion+1)<<" ";

    outFile<<(podRegion)<<endl;

}
void test(fstream &outFile, int test,long long n,long long k);

void heapCalc(fstream &outFile, int testNr, long long n,long long k)
{
  long long  myints[] = {n};
  std::vector<long long> v(myints,myints+1);

  std::make_heap (v.begin(),v.end());

  for(long long i=0;i<k-1;++i)
  {
    long long tmp = v.front();
    std::pop_heap (v.begin(),v.end()); v.pop_back();
    tmp--;
    long long half = tmp>>1;
    
    v.push_back(half); std::push_heap (v.begin(),v.end());

    if (tmp%2 == 0)
    {
        v.push_back(half); std::push_heap (v.begin(),v.end());
    }
    else 
    {
        v.push_back(half+1); std::push_heap (v.begin(),v.end());
    }

  }
    long long maxRegion = v.front();
    maxRegion--;

    long long podRegion = maxRegion>>1;
    
    //cout<<maxRegion<<endl;
    outFile<<"Case #"<<testNr<<": ";

    if(maxRegion%2 == 0)
        outFile<<podRegion<<" ";
    else
        outFile<<(podRegion+1)<<" ";

    outFile<<(podRegion)<<endl;
}
int main()
{
    fstream outFile("c.out",fstream::out);

    int tests;
    cin>>tests;

    for(int test=1;test<=tests;++test)
    {
        cout<<test<<endl;
        long long n,k;
        cin>>n>>k;
        //calc(outFile,test,n,k);
        heapCalc(outFile,test,n,k);
    }
/*
    test(outFile,0,1000,489);
    test(outFile,0,500,67);
    test(outFile,0,361,359);
    test(outFile,0,500,117);
    */

}
void test(fstream &outFile, int test,long long n,long long k)
{
    calc1(outFile,0,n,k);
    heapCalc(outFile,0,n,k);
}