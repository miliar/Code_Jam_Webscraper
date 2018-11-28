#include <iostream>
#include <cmath>
#include <list>

using namespace std;

class StallDistance {
private:
  unsigned long long mLs;
  unsigned long long mRs;

public:
  StallDistance() : mLs(0), mRs(0) {};
  StallDistance(unsigned long long Ls, unsigned long long Rs) : mLs(Ls), mRs(Rs) {};

  unsigned long long getLs() { return mLs; }
  unsigned long long getRs() { return mRs; }
  unsigned long long getMin() { return mLs < mRs? mLs : mRs; }
  unsigned long long getMax() { return mLs < mRs? mRs : mLs; }

  bool needsReplace(unsigned long long Ls, unsigned long long Rs) {
    unsigned long long min = (Ls < Rs? Ls:Rs);
    unsigned long long lmin = (mLs < mRs? mLs:mRs);
    unsigned long long max = (Ls < Rs? Rs:Ls);
    unsigned long long lmax = (mLs < mRs? mRs:mLs);
    // cout << "min: " << min << " max: " << max << endl;
    // cout << "lmin: " << lmin << " lmax: " << lmax << endl;
    if (min == lmin)
      return max > lmax;
    return (min > lmin);
  }
  void reset(unsigned long long Ls, unsigned long long Rs) {
    mLs = Ls;
    mRs = Rs;
  }
  
  void print() { cout << "mLs: " << mLs << " mRs: " << mRs << endl; }

};

StallDistance selectStall(list<unsigned long long>& bathroomList) {
  list<unsigned long long>::iterator ci = bathroomList.begin();
  unsigned long long lhsStallId = *ci;
  unsigned long long rhsStallId;
  StallDistance selectedStall;
  list<unsigned long long>::iterator markerItr = ci;
  while (++ci != bathroomList.end()) {
    rhsStallId = *ci;
    // cout << "lhsStallId: " << lhsStallId << " rhsStallId: " << rhsStallId << endl;
    if ((rhsStallId - lhsStallId) > 1) {
      // cout << "Ls: " << (rhsStallId + lhsStallId)/2 - lhsStallId << " Rs: " << rhsStallId - (rhsStallId + lhsStallId)/2 << endl;
      if (selectedStall.needsReplace((rhsStallId + lhsStallId)/2 - lhsStallId, rhsStallId - (rhsStallId + lhsStallId)/2)) {
         selectedStall.reset((rhsStallId + lhsStallId)/2 - lhsStallId, rhsStallId - (rhsStallId + lhsStallId)/2);
         markerItr = ci;
         // selectedStall.print();
      }
    }
    if (ci != bathroomList.end()) {
      lhsStallId = rhsStallId;
    }
  }
  // cout << "Marker: " << *markerItr << endl;
  bathroomList.insert(markerItr, *markerItr - selectedStall.getRs()); 
  return selectedStall;
}

int main(int argc, char* argv[]) 
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    unsigned long long N, K;
    cin >> N >> K;
    list<unsigned long long> bathroomStalls;
    bathroomStalls.push_back(0ULL);
    bathroomStalls.push_back(N + 1);
    cout << "N: " << N << " K: " << K << endl;
    StallDistance final; 
    for (unsigned long long ii = 0; ii < K; ++ii) {
      final = selectStall(bathroomStalls);
    /*for (list<unsigned long long>::const_iterator ci = bathroomStalls.begin(); ci != bathroomStalls.end(); ++ci)
      cout << *ci << " ";
    cout << endl;*/
    }
    cout << "Case #" << i << ": " << final.getMax() - 1 << " " << final.getMin() - 1 << endl;
  }
  return 0;
}
