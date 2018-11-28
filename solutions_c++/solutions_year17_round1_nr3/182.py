#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;


int licz(int hd, int ad, int hk, int ak, int b, int d, int bb, int dd)
{
    int wyn=0, ohd=hd;
    for (int i=0; i<dd && 0<ak; ++i)
    {
        int nak=max(0, ak-d);
        int nhd=hd-nak;
        if (0<nhd)
        {
            ak=nak;
            hd=nhd;
        }
        else
        {
            hd=ohd-ak;
            if (hd<=0)
                return MaxInt;
        }
        ++wyn;
    }

    for (int i=0; i<bb; ++i)
    {
        if (hd-ak<=0) hd=ohd-ak;
        else
        {
            ad+=b;
            hd-=ak;
        }
        if (hd<=0)
            return MaxInt;
        ++wyn;
    }

    int lz=0;
    for (; ; )
    {
        ++wyn;
        if (hk<=ad)
            break;
        if (hd-ak<=0)
        {
            hd=ohd-ak;
            ++lz;
        }
        else
        {
            lz=0;
            hk-=ad;
            hd-=ak;
        }
        if (hd<=0 || 5<lz)
            return MaxInt;
    }

    return wyn;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
      int hd, ad, hk, ak, b, d;
      cin>>hd>>ad>>hk>>ak>>b>>d;
      int wyn=MaxInt;
      for (int dd=0; dd<=202; ++dd)
          for (int bb=0; bb<=202; ++bb)
              wyn=min(wyn, licz(hd, ad, hk, ak, b, d, bb, dd));
      cout<<"Case #"<<ca<<": ";
      if (wyn==MaxInt) cout<<"IMPOSSIBLE";
      else cout<<wyn;
      cout<<endl;
  }

  return 0;
}
