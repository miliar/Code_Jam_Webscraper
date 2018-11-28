#include <fstream>

using namespace std;

int main()
{
    ifstream ifs("A-large.in");
    ofstream ofs("A-large.out");

    int T;
    ifs >> T;

    for(int i=0; i<T; i++)
    {
        string buf;
        ifs >> buf;

        int K;
        ifs >> K;

        int len = buf.size();
        int count = 0;
        for(int j=0; j<len-K+1; j++)
        {
            if(buf[j]=='-')
            {
                for(int k=0; k<K; k++)
                {
                    buf[j+k] = buf[j+k]=='+'? '-' : '+';
                }
                count++;
            }
        }

        bool possible = true;
        for(int j=0; j<K; j++)
        {
            possible &= buf[len-j-1]=='+';
        }

        ofs << "Case #" << i+1 << ": ";
        if(possible)
        {
            ofs << count << endl;
        }
        else
        {
            ofs << "IMPOSSIBLE" << endl;
        }
    }
}
