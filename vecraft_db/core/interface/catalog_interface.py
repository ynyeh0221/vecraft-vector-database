
from abc import ABC, abstractmethod
from typing import List

from vecraft_data_model.index_packets import CollectionSchema


class Catalog(ABC):

    @abstractmethod
    def create_collection(self, collection_schema: CollectionSchema) -> CollectionSchema:
        ...

    @abstractmethod
    def drop_collection(self, name: str) -> CollectionSchema:
        ...

    @abstractmethod
    def list_collections(self) -> List[CollectionSchema]:
        ...

    @abstractmethod
    def get_schema(self, name: str) -> CollectionSchema:
        ...

    def shutdown(self):
        ...