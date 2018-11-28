#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("in.txt");
    streambuf *cinbuf = cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    ofstream out("out.txt");
    streambuf *coutbuf = cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!


    int T;
    cin >> T;

    for(int i=0;i<T;++i)
    {
        int N;
        double D;
        cin>>D>>N;
        double K[N];
        double S[N];
        for(int j=0;j<N;++j)
        {
            cin>>K[j]>>S[j];
        }
        double max=0;
        for(int j=0;j<N;++j)
        {
            if(max<((D-K[j])/S[j]))
            {
                max=(D-K[j])/S[j];
            }
        }
        cout.precision(15);
        cout<<"Case #"<<i+1<<": "<<D/max<<endl;
    }


/*
    int count;
    cin >> count;
    int * array = new int[count];
    for (int i=0; i<count; i++)
        cin >> array[i];


    delete [] array;
 */
    return 0;
}
