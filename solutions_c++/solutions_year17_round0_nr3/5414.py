#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <vector>

struct toiletStall
{
   bool occupied;
   int position;
   int emptyShittersLeft;
   int emptyShittersRight;
   int closestNeighborDist;
   int farthestNeighborDist;
};

typedef struct toiletStall Toilet;

Toilet* findEmptyShitter(std::vector<Toilet*>* br)
{
   std::vector<Toilet*> prospects;

   for(auto pottyIter = br->begin(); pottyIter != br->end(); pottyIter++)
   {
      if ((*pottyIter)->occupied)
         continue;

      //std::cerr << "Toilet #" << (*pottyIter)->position << " is unoccupied" << std::endl;
      if (prospects.empty())
      {
         // Well, this is better than using the sink right?
         prospects.push_back(*pottyIter);
         //std::cerr << "Well, " << (*pottyIter)->position << " is better than the sink! " << (*pottyIter)->closestNeighborDist << std::endl;
      }
      else
      {
         // Is this better than the other toilets?
         if (prospects.front()->closestNeighborDist > (*pottyIter)->closestNeighborDist)
         {
            //std::cerr << "Closest person to stall #" <<  (*pottyIter)->position << " is to close! " << (*pottyIter)->closestNeighborDist << std::endl;
         }
         else if (prospects.front()->closestNeighborDist == (*pottyIter)->closestNeighborDist)
         {
            //std::cerr << "Another good prospect at #" << (*pottyIter)->position << std::endl;
            prospects.push_back(*pottyIter);
         }
         else
         {
            // new best toilet
            //std::cerr << "Toilet " << (*pottyIter)->position << " is the new best! " << (*pottyIter)->closestNeighborDist << std::endl;
            prospects.clear();

            prospects.push_back(*pottyIter);
         }
      }
   }

   if (prospects.size() == 1)
   {
      //std::cerr << "One candidate out shits the rest: " << prospects.front()->position << std::endl;
      return prospects.front();
   }

   Toilet* retVal = prospects.front();
   for(int i = 1; i < prospects.size(); i++)
   {
      if (retVal->farthestNeighborDist < prospects[i]->farthestNeighborDist)
      {
         retVal = prospects[i];
      }
   }

   //std::cerr << "It was close, but we are choosing toilet " << retVal->position << std::endl;
   return retVal;
}

void updateMinAndMax(Toilet* t)
{
   if (t->emptyShittersLeft > t->emptyShittersRight)
   {
      t->closestNeighborDist = t->emptyShittersRight;
      t->farthestNeighborDist = t->emptyShittersLeft;
   }
   else
   {
      t->closestNeighborDist = t->emptyShittersLeft;
      t->farthestNeighborDist = t->emptyShittersRight;
   }
}

void insertNewShitter(std::vector<Toilet*>* br, int position)
{
   Toilet* winner = (*br)[position];
   winner->occupied = true;
   winner->emptyShittersLeft = -1;
   winner->emptyShittersRight = -1;
   winner->farthestNeighborDist = -1;
   winner->closestNeighborDist = -1;

   for(int i = position - 1; i >= 0; i--)
   {
      // Updating toilets to the left of our stall
      Toilet* ts = (*br)[i];

      if (!ts->occupied)
      {
         ts->emptyShittersRight = position - i - 1;
         updateMinAndMax(ts);
      }
      else
      {
         // Find one occupied, we are done
         break;
      }
   }

   for(int i = position + 1; i < br->size(); i++)
   {
      // Updating toilets to the right of our stall
      Toilet* ts = (*br)[i];

      if (!ts->occupied)
      {
         ts->emptyShittersLeft = i - position - 1;
         updateMinAndMax(ts);
      }
      else
      {
         // Find one occupied, we are done
         break;
      }
   }
}

void initializeToilets(std::vector<Toilet*>* br, int numToilets)
{
   for(int i = 0; i < numToilets; i++)
   {
      Toilet* ts = new Toilet();
      ts->occupied = false;
      ts->emptyShittersLeft = i;
      ts->emptyShittersRight = numToilets - i - 1;
      ts->position = i;

      updateMinAndMax(ts);

      br->push_back(ts);
   }
}

void printBathroomDetails(std::vector<Toilet*>* br)
{
   for(auto stall = br->begin(); stall != br->end(); stall++)
   {
      std::cerr << "Toilet #" << (*stall)->position << ", occupied=" << ((*stall)->occupied ? "Yes" : "No") << ", EmptyLeft="
                << (*stall)->emptyShittersLeft << ", EmptyRight=" << (*stall)->emptyShittersRight << ", Min="
                << (*stall)->closestNeighborDist << ", Max=" << (*stall)->farthestNeighborDist << std::endl;
   }
}


std::string solveCase()
{
   int numTurdReceivers = 0;
   std::cin >> numTurdReceivers;

   std::vector<Toilet*> bathroom;
   initializeToilets(&bathroom, numTurdReceivers);

   //printBathroomDetails(&bathroom);

   int numPeopleDeucing = 0;
   std::cin >> numPeopleDeucing;

   int retMin;
   int retMax;
   for(int i = 0; i < numPeopleDeucing; i++)
   {
      Toilet* anEmpty = findEmptyShitter(&bathroom);
      retMin = anEmpty->closestNeighborDist;
      retMax = anEmpty->farthestNeighborDist;

      insertNewShitter(&bathroom, anEmpty->position);

      //printBathroomDetails(&bathroom);
   }

   std::ostringstream oss;
   oss << retMax << " " << retMin;
   return oss.str();

}

int main(int, char**)
{
   int numCases = 0;
   std::cin >> numCases;

   for(int i = 0; i < numCases; i++)
   {
      std::cout << "Case #" << i+1 << ": " << solveCase() << std::endl;
   }

   return 0;
}
