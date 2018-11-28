
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <stdlib.h>
#include <numeric>
#include <math.h>
#include <queue>
#include <algorithm>

struct node {
  unsigned minI;
  unsigned maxI;
  unsigned id;
};

struct CompareNodes
{
  bool operator()(node const & n1, node const & n2)
  {
    if ( (n1.maxI - n1.minI) == (n2.maxI - n2.minI))
      return n1.id > n2.id;
    else
      return (n1.maxI - n1.minI) < (n2.maxI - n2.minI);
  }
};

using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main()
{
  unsigned num, numStalls, numUsers;
  cin >> num;

  for (unsigned i = 1; i <= num; ++i)
  {
    cin >> numStalls >> numUsers;

    queue<unsigned> qStallIndices;
    bool even = (numStalls%2 == 0);

    std::vector<node> nodesV(numStalls);
    unsigned nodeI = 0;
    nodesV[nodeI].minI = 0;
    nodesV[nodeI].maxI = numStalls - 1;
    nodesV[nodeI].id = nodeI;

    priority_queue<node, std::vector<node>, CompareNodes> pQBreadth;
    pQBreadth.push(nodesV[nodeI]);
    queue<node> parentQueue;
    vector<unsigned> processLast;
    parentQueue.push(nodesV[nodeI]);

    while (!parentQueue.empty())
    {
      if (qStallIndices.size() == numUsers) break;

      while (!pQBreadth.empty())
      {
        node parent = pQBreadth.top();
        if (!even && (parent.minI == parent.maxI))
        {
          std::vector<unsigned>::iterator it = std::upper_bound(processLast.begin(), processLast.end(), parent.maxI); //1
          processLast.insert(it, parent.maxI);
        }

        else
        {
          unsigned middleI = parent.minI + (parent.maxI-parent.minI)/2;
          qStallIndices.push(middleI);
          if (qStallIndices.size() == numUsers) break;
        }
        pQBreadth.pop();
      }

      unsigned sizeq = parentQueue.size();
      node parent;
      for (unsigned count = 0; count < sizeq; count++)
      {
        parent = parentQueue.front();
        unsigned middleI = parent.minI + (parent.maxI-parent.minI)/2;

        // Left child
        if (middleI != parent.minI)
        {
          nodeI++;
          nodesV[nodeI].minI = parent.minI;
          nodesV[nodeI].maxI = middleI - 1;
          nodesV[nodeI].id = nodeI;
          parentQueue.push(nodesV[nodeI]);
          pQBreadth.push(nodesV[nodeI]);

//          if (!even && (nodesV[nodeI].minI == nodesV[nodeI].maxI))
//            processLast.push(nodesV[nodeI]);
//
//          else
//            pQBreadth.push(nodesV[nodeI]);

        }

        // Right child
        if (middleI != parent.maxI)
        {
          nodeI++;
          nodesV[nodeI].minI = middleI + 1;
          nodesV[nodeI].maxI = parent.maxI;
          nodesV[nodeI].id = nodeI;
          parentQueue.push(nodesV[nodeI]);
          pQBreadth.push(nodesV[nodeI]);

//          if (!even && (nodesV[nodeI].minI == nodesV[nodeI].maxI))
//            processLast.push(nodesV[nodeI]);
//
//          else
//            pQBreadth.push(nodesV[nodeI]);
        }

        parentQueue.pop();
      }
    }

    for (vector<unsigned>::iterator it = processLast.begin(); it != processLast.end(); it++)
    {
      if (qStallIndices.size() == numUsers) break;
      qStallIndices.push(*it);
    }

    // non-priority queue

//      queue<node> qBreadth;
//      qBreadth.push(nodesV[0]);
//
//
//      while (!qBreadth.empty())
//      {
//        if (qStallIndices.size() == numUsers) break;
//
//        node parent = qBreadth.front();
//        qBreadth.pop();
//        unsigned middleI = parent.minI + (parent.maxI-parent.minI)/2;
//        qStallIndices.push(middleI);
//
//        // Left child
//        if (middleI != parent.minI)
//        {
//          node leftChild;
//          leftChild.minI = parent.minI;
//          leftChild.maxI = middleI - 1;
//          qBreadth.push(leftChild);
//        }
//
//        // Right child
//        if (middleI != parent.maxI)
//        {
//          node rightChild;
//          rightChild.minI = middleI + 1;
//          rightChild.maxI = parent.maxI;
//          qBreadth.push(rightChild);
//        }
//      }
//    }

    if (qStallIndices.size() != numUsers) exit(-1);

    unsigned lastStallI = qStallIndices.back();
    unsigned left = lastStallI;
    unsigned right = numStalls - lastStallI - 1;

    while (qStallIndices.size() > 1)
    {
      unsigned stallI = qStallIndices.front();
      qStallIndices.pop();
      unsigned newR, newL;

      if (stallI < lastStallI)
      {
        newL = lastStallI - stallI - 1;
        newR = right;
      }

      else if (stallI > lastStallI)
      {
        newL = left;
        newR = stallI - lastStallI - 1;
      }
      else
      {
        exit(-1);
      }

      // update latest l & r
      if (newL < left) left = newL;
      if (newR < right) right = newR;
    }

    unsigned max, min;
    if (left > right)
    {
      max = left;
      min = right;
    }
    else
    {
      max = right;
      min = left;
    }

    cout << "Case #" << i << ": " << max << " " << min << endl;

  }

  return 0;
}
